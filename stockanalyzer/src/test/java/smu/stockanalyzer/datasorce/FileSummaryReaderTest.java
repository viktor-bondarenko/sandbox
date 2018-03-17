package smu.stockanalyzer.datasorce;

import org.hamcrest.Matchers;
import org.junit.Test;
import org.junit.matchers.JUnitMatchers;
import smu.stockanalyzer.model.Stock;
import java.util.List;

import static org.hamcrest.Matchers.greaterThan;
import static org.junit.Assert.*;

public class FileSummaryReaderTest {

    @Test
    public void getStocks() {
        FileSummaryReader fileSummaryReader = new FileSummaryReader();
        List<Stock> stocks = fileSummaryReader.getStocks();
        assertThat(stocks, Matchers.hasSize(greaterThan(6000)));
    }
}