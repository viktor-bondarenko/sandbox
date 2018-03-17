package smu.stockanalyzer.datasorce;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVRecord;
import org.apache.commons.lang3.StringUtils;
import smu.stockanalyzer.model.Stock;
import java.io.FileReader;
import java.io.IOException;
import java.io.Reader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;
import java.util.stream.StreamSupport;

public class FileSummaryReader implements StockReader {

    private String filePath = "/Users/vbondarenko/Documents/inv/stocks.csv";

    public FileSummaryReader() {
    }

    public FileSummaryReader(String filePath) {
        this.filePath = filePath;
    }

    private Stock toStock(CSVRecord record) {
        Stock stock = new Stock();
        if (record != null) {
            stock.setSymbol(record.get(0));
            stock.setName(record.get(1));
            ArrayList<Double> prices = new ArrayList<>();
            String priceString = record.get(2);
            if (!StringUtils.equalsIgnoreCase(priceString, "n/a")) {
                prices.add(Double.parseDouble(priceString));
            }
            stock.setPrices(prices);

            ArrayList<Double> marketCaps = new ArrayList<>();
            String marketCapString = record.get(3);
            if (!StringUtils.equalsIgnoreCase(marketCapString, "n/a")) {
                String marketCapMeasurement = marketCapString.substring(marketCapString.length() - 1);
                int multiplier = 1;
                switch (marketCapMeasurement) {
                    case "M":
                        multiplier = 1000000;
                        marketCapString = marketCapString.substring(1, marketCapString.length() - 1);
                        break;
                    case "B":
                        multiplier = 1000000000;
                        marketCapString = marketCapString.substring(1, marketCapString.length() - 1);
                        break;
                    default:
                        System.out.println("unknown market cap measurement - " + marketCapMeasurement + ", " + marketCapString);
                        marketCapString = marketCapString.substring(1);

                }

                Double marketCap = Double.parseDouble(marketCapString) * multiplier;
                marketCaps.add(marketCap);
            }
            stock.setMarketCaps(marketCaps);
        }
        return stock;
    }

    public List<Stock> getStocks() {
        List<Stock> stocks = Collections.emptyList();
        try (Reader in = new FileReader(filePath)) {
            Iterable<CSVRecord> records = CSVFormat.EXCEL.parse(in);
            Stream<CSVRecord> csvRecordStream = StreamSupport.stream(records.spliterator(), false);
            stocks = csvRecordStream.map(this::toStock).collect(Collectors.toList());
            for (CSVRecord record : records) {
                System.out.println(record);
//                stocks.add(toStock(record));
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        return stocks;
    }
}
