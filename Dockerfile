# Usa la imagen de alpine como base
FROM node:14-alpine

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu aplicación al directorio de trabajo del contenedor
COPY package.json package-lock.json /app/
COPY server.js /app/

# Instala las dependencias
RUN npm install

# Expone el puerto 3000 para que pueda accederse desde fuera del contenedor
EXPOSE 3000

# Comando para iniciar la aplicación cuando se ejecute el contenedor
CMD ["node", "server.js"]

