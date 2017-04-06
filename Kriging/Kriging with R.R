# rm(list = ls())

calidata <- read.csv("Kriging Train Data.csv")

install.packages("sp")
install.packages("gstat")

library(sp)
library(gstat)
library(dplyr)
library(ggplot2)
library(scales)
library(magrittr)
library(gridExtra)

glimpse(calidata)

calidata <- within(calidata, rm(X))

glimpse(calidata)

# Initial plot of Zn concentration in California
calidata %>% as.data.frame %>%
  ggplot(aes(Longitude, Latitude)) +
  geom_point(aes(size = Zn),
             color = "forestgreen",
             alpha = 0.75) +
  ggtitle("Zinc Concentration (ppm)") +
  coord_equal()

# Remove rows where columns of interest have NA values
nasremoved <- complete.cases(calidata[, c("Zn", "Longitude", "Latitude")])
krigedata <- calidata[nasremoved, ]

# Convert data to spatial points dataframe
coordinates(krigedata) <- ~ Longitude + Latitude

# View bounding box of data
bbox(krigedata)

# Check coordinates
coordinates(krigedata)

# Check data
krigedata@data %>% glimpse

# Coerce data into a dataframe, i.e. for ggplot2
# kridgedata %>% as.data.frame

### Variogram Fitting

samplevario <- variogram(log(Zn) ~ 1, krigedata)
plot(samplevario, main = "Sample Semivariogram")

fitmodel <- fit.variogram(samplevario, model = vgm("Sph"))
plot(samplevario, fitmodel, main = "Fitted Semivariogram")

### Kriging

# Spatial domain to interpolate over
test <- read.csv("Kriging Test Data.csv")

# Plot points with measurements
knownpoints <- krigedata %>% as.data.frame %>%
  ggplot(aes(Longitude, Latitude)) +
  geom_point(size = 1) +
  coord_equal() +
  ggtitle("Points with measurements")
knownpoints

# Plot points to interpolate (krige) over
unknownpoints <- test %>% as.data.frame %>%
  ggplot(aes(Longitude, Latitude)) + 
  geom_point(size = 1) + 
  coord_equal() + 
  ggtitle("Points to krige")
unknownpoints

# View plots side-by-side
grid.arrange(knownpoints, unknownpoints, ncol = 2)

# Convert spatial domain into an SPDF
coordinates(test) <- ~ Longitude + Latitude

# Remove duplicate coordinates
krigedata <- krigedata[-zerodist(krigedata)[,1],]
test <- test[-zerodist(test)[,1],]

# Universal kriging (assume linear dependence on coordinates)
krigedmodel <- krige(log(Zn) ~ 1,
                     krigedata, test,
                     model = fitmodel)

krigedmodel%>% as.data.frame %>% glimpse

# Heat mapping
krigedmodel %>% as.data.frame %>%
  ggplot(aes(x=Longitude, y=Latitude)) +
  geom_point(aes(color = var1.pred), alpha = 0.7) + 
  coord_equal() + 
  scale_color_gradient(low = "yellow", high = "red") +
  scale_x_continuous(labels = comma) +
  scale_y_continuous(labels = comma) +
  theme_bw()

testwithactuals <- read.csv("Kriging Test Data with Actual Values.csv")
coordinates(testwithactuals) <- ~ Longitude + Latitude
testwithactuals <- testwithactuals[-zerodist(testwithactuals)[,1],]
