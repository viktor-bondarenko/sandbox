package smu.stockanalyzer.model;

import java.util.Date;
import java.util.List;

public class DividendsInfo {
    Date since;
    Integer yearsGrows;
    Double currentYield;
    List<DividendRecord> dividendsHistory;
}
