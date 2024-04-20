const express = require('express');
const app = express();
const PORT = 3000;

app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.post('/calcular-imc', (req, res) => {
    const peso = parseFloat(req.body.peso);
    const altura = parseFloat(req.body.altura);

    const imc = peso / (altura * altura);

    res.json({ imc: imc.toFixed(2) });
});

app.listen(PORT, () => {
    console.log(`Servidor Express corriendo en http://localhost:${PORT}`);
});
