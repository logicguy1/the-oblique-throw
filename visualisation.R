library(readr)
data <- read_csv("documents/scripting/fysss/data.csv")
View(data)

summary(data)
str(data)

library(ggplot2)
ggplot(data = data, aes(x = vel, y = ang, color = dist)) + 
  geom_point() + # The way the plot should look
  scale_colour_gradientn(colours=rainbow(6)) +
  labs(title = "The distance traveled corrosponding to angle and velocety",
       x = "Velocety at launch [m/s]",
       y = "Angle [degrees]"
  )

ggsave("Crazyplot.png")

subs <- subset(data, dist == max(data)) # Get the higest point
ggplot(data = subs, aes(x = vel, y = ang, color = dist)) + 
  geom_point() + # The way the plot should look
  labs(title = "The distance traveled corrosponding to angle and velocety",
       x = "Velocety at launch [m/s]",
       y = "Angle [degrees]"
  )

