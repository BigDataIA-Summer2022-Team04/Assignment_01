# This is a reproduction of peter.aldhous@buzzfeed.com foridentifying potential surveillance aircraft
# Link: https://buzzfeednews.github.io/2017-08-spy-plane-finder/
# 


# load required packages
library(readr)
library(dplyr)
library(randomForest)

# load planes_features data
planes <- read_csv("/Users/piyush/Sandbox/DAMG7245_Assignment_01/data/raw/planes_features.csv") 

# convert type to integers, as new variable type2, so it can be used by the random forest algorithm
planes <- planes %>%
  mutate(type2=as.integer(as.factor(type)))

# load training data and join to the planes_features data
train <- read_csv("/Users/piyush/Sandbox/DAMG7245_Assignment_01/data/raw/train.csv") %>%
  inner_join(planes, by="adshex")

# set seed for reproducibility of model fit
set.seed(415)

# train the random forest
fit <- randomForest(as.factor(class) ~ duration1 + duration2 + duration3 + duration4 + duration5 + boxes1 + boxes2 + boxes3 + boxes4 + boxes5 + speed1 + speed2 + speed3 + speed4 + speed5 + altitude1 + altitude2 + altitude3 + altitude4 + altitude5 + steer1 + steer2 + steer3 + steer4 + steer5 + steer6 + steer7 + steer8 + flights + squawk_1 + observations + type2,
                    data=train, 
                    importance=TRUE,
                    ntree=2000)

# look at which variables are important in model
varImpPlot(fit, pch = 19, main = "Importance of variables", color = "blue", cex = 0.7)

# look at estimated model performance
print(fit)

# Call:
#   randomForest(formula = as.factor(class) ~ duration1 + duration2 +      duration3 + duration4 + duration5 + boxes1 + boxes2 + boxes3 +      boxes4 + boxes5 + speed1 + speed2 + speed3 + speed4 + speed5 +      altitude1 + altitude2 + altitude3 + altitude4 + altitude5 +      steer1 + steer2 + steer3 + steer4 + steer5 + steer6 + steer7 +      steer8 + flights + squawk_1 + observations + type2, data = train,      importance = TRUE, ntree = 2000) 
# Type of random forest: classification
# Number of trees: 2000
# No. of variables tried at each split: 5
# 
# OOB estimate of  error rate: 3.69%
# Confusion matrix:
#   other surveil class.error
# other     498       2   0.0040000
# surveil    20      77   0.2061856

# load data on known federal planes
feds <- read_csv("/Users/piyush/Sandbox/DAMG7245_Assignment_01/data/raw/feds.csv")

# create dataset to classify
classify <- anti_join(planes, train) %>%
  anti_join(feds)

# run the random forest model on that dataset
prediction <- predict(fit, classify)

# create data frame with predictions from random forest, by plane
classified <- data.frame(adshex = classify$adshex, class = prediction)


# summarize to see how many planes classified as candidate surveillance aircraft
classified_summary <- classified %>%
  group_by(class) %>%
  summarize(count=n())
print(classified_summary)
# # A tibble: 2 × 2
# class   count
# <fct>   <int>
# 1 other   19085
# 2 surveil    75

# run the random forest model again to get probabilities of membership of each class, rather than binary classification
prediction_probs <- as.data.frame(predict(fit, classify, type = "prob"))

# create data frame with predictions from random forest, by plane
classified_probs <- bind_cols(as.data.frame(classify$adshex), prediction_probs) %>%
  mutate(adshex = classify$adshex) %>%
  select(2:4) %>%
  arrange(desc(surveil)) %>%
  inner_join(planes) %>%
  select(1:3,squawk_1)

# select the top 100 candidates
candidates <- head(classified_probs, 100)

# load and process FAA registration data (here using download from Jul 25, 2017, to reflect current registration)
faa <- read_csv("/Users/piyush/Sandbox/DAMG7245_Assignment_01/data/raw/faa_registration.csv") %>%
  select(1,7,34)
names(faa) <- c("n_number","name","adshex")
faa <- faa %>%
  mutate(reg = paste0("N",n_number)) %>%
  select(2:4)

# join to FAA registration data to obtain information on each plane's registration numbers and registered owners/operators
candidates <- left_join(candidates,faa, by="adshex")

# export data
write_csv(candidates, "/Users/piyush/Sandbox/DAMG7245_Assignment_01/data/processed/candidates.csv", na="")
