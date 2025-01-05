import express from 'express';
import fs from 'fs';
import { parse } from 'csv-parse';
import { stringify } from 'csv-stringify';

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended: true }));

app.post('/data', (req, res) => {
  const { data } = req.body;
  const [current, power] = data.split(',');
  const timestamp = new Date().toISOString();

  const csvData = `${timestamp},${current},${power}\n`;

  fs.appendFile('electricity_data.csv', csvData, (err) => {
    if (err) {
      console.error('Error writing to CSV:', err);
      res.status(500).send('Error saving data');
    } else {
      console.log('Data saved to CSV');
      res.status(200).send('Data received and saved');
    }
  });
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});

