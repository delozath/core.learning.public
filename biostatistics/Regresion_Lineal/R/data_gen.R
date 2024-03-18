# Establecer una semilla para reproducibilidad
set.seed(123)

# Generar los datos sintéticos
n <- 30
id <- 1:n
edad <- rnorm(n, mean = 30, sd = 5)
educacion <- rnorm(n, mean = 12, sd = 3)
experiencia <- rnorm(n, mean = 5, sd = 2)
productividad <- rnorm(n, mean = 10, sd = 2)
salario <- 1000 + 500 * experiencia + 200 * productividad + rnorm(n, mean = 0, sd = 100)

# Crear un data frame con los datos sintéticos y etiquetar las variables
datos_sinteticos <- data.frame(id, edad, educacion, experiencia, productividad, salario)
names(datos_sinteticos) <- c("ID", "Edad", "Educación", "Experiencia", "Productividad", "Salario")

# Guardar los datos sintéticos en un archivo CSV
write.csv(datos_sinteticos, file = "datos_sinteticos.csv", row.names = FALSE)





# Establecer una semilla para reproducibilidad
set.seed(123)

# Generar los datos sintéticos
n <- 50
id <- 1:n
edad <- rnorm(n, mean = 30, sd = 5)
altura <- rnorm(n, mean = 170, sd = 10)
peso <- rnorm(n, mean = 70, sd = 5)
cintura <- rnorm(n, mean = 80, sd = 5)
cadera <- rnorm(n, mean = 100, sd = 5)
presion_sistolica <- rnorm(n, mean = 120, sd = 10)
presion_diastolica <- rnorm(n, mean = 80, sd = 5)
salud <- rnorm(n, mean = 50 + 0.5 * edad - 1.5 * cadera + presion_sistolica + rnorm(n, mean = 0, sd = 5))

# Crear un data frame con los datos sintéticos y etiquetar las variables
datos_sinteticos <- data.frame(id, 
                               edad, 
                               altura, 
                               peso, 
                               Cintura = cintura, 
                               Cadera = cadera, 
                               `Presión Sistólica` = presion_sistolica, 
                               `Presión Diastólica` = presion_diastolica, 
                               `Salud Mental` = salud)
names(datos_sinteticos) <- c("ID", 
                             "Edad", 
                             "Altura", 
                             "Peso", 
                             "Cintura", 
                             "Cadera", 
                             "Presión Sistólica", 
                             "Presión Diastólica", 
                             "Salud")

# Guardar los datos sintéticos en un archivo CSV
write.csv(datos_sinteticos, file = "salud_1.csv", row.names = FALSE)



# Establecer una semilla para reproducibilidad
set.seed(123)

# Generar los datos sintéticos
n <- 50
id <- 1:n
edad <- rnorm(n, mean = 30, sd = 5)
altura <- rnorm(n, mean = 170, sd = 10)
peso <- rnorm(n, mean = 70, sd = 5)
cintura <- rnorm(n, mean = 80, sd = 5)
cadera <- rnorm(n, mean = 100, sd = 5)
presion_sistolica <- rnorm(n, mean = 120, sd = 10)
presion_diastolica <- rnorm(n, mean = 80, sd = 5)
salud <- rnorm(n, mean = 50, sd = 10)

# Crear un data frame con los datos sintéticos y etiquetar las variables
datos_sinteticos <- data.frame(id, 
                               edad, 
                               altura, 
                               peso, 
                               Cintura = cintura, 
                               Cadera = cadera, 
                               `Presión Sistólica` = presion_sistolica, 
                               `Presión Diastólica` = presion_diastolica, 
                               `Salud Mental` = salud)
names(datos_sinteticos) <- c("ID", 
                             "Edad", 
                             "Altura", 
                             "Peso", 
                             "Cintura", 
                             "Cadera", 
                             "Presión Sistólica", 
                             "Presión Diastólica", 
                             "Salud")

# Guardar los datos sintéticos en un archivo CSV
write.csv(datos_sinteticos, file = "salud_2.csv", row.names = FALSE)
