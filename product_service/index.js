const express = require('express');
const mongoose = require('mongoose');
const app = express();
const PORT = 3000;

app.use(express.json());

mongoose.connect('mongodb://localhost:27017/products', { useNewUrlParser: true, useUnifiedTopology: true });

const productSchema = new mongoose.Schema({
    name: String,
    price: Number
});

const Product = mongoose.model('Product', productSchema);

// POST API to add a new product
app.post('/products', async (req, res) => {
    try {
        const product = new Product(req.body);
        await product.save();
        res.status(201).send({
            message: 'Product successfully added',
            product: product
        });
    } catch (error) {
        res.status(400).send({ error: 'Error adding product', details: error.message });
    }
});

app.get('/products', async (req, res) => {
    try {
        const products = await Product.find(); 
        res.status(200).send({
            message: 'Products retrived successfully',
            product: products
        });
    } catch (error) {
        res.status(500).send({ error: 'Error retrieving products', details: error.message });
    }
});

app.listen(PORT, () => {
    console.log(`Product service running on port ${PORT}`);
});
