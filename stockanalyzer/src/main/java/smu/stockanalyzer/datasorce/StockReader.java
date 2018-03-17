package smu.stockanalyzer.datasorce;

import smu.stockanalyzer.model.Stock;
import java.util.List;

public interface StockReader {
    List<Stock> getStocks();
}
