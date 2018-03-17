package smu.stockanalyzer.model;

import org.apache.commons.lang3.builder.EqualsBuilder;
import org.apache.commons.lang3.builder.HashCodeBuilder;
import java.util.List;

public class Stock {
    private Long id;
    private String symbol;
    private String name;
    private List<Double> prices;
    private List<Double> marketCaps;
    private Integer ipoYear;
    private Sector sector;
    private Industry industry;
    private String summaryQuote;
    private DividendsInfo dividendsInfo;

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;

        if (!(o instanceof Stock)) return false;

        Stock stock = (Stock) o;

        return new EqualsBuilder()
                .append(getSymbol(), stock.getSymbol())
                .append(getName(), stock.getName())
                .append(getPrices(), stock.getPrices())
                .append(getMarketCaps(), stock.getMarketCaps())
                .append(getIpoYear(), stock.getIpoYear())
                .append(getSector(), stock.getSector())
                .append(getIndustry(), stock.getIndustry())
                .append(getSummaryQuote(), stock.getSummaryQuote())
                .append(getDividendsInfo(), stock.getDividendsInfo())
                .isEquals();
    }

    @Override
    public int hashCode() {
        return new HashCodeBuilder(17, 37)
                .append(getSymbol())
                .append(getName())
                .append(getPrices())
                .append(getMarketCaps())
                .append(getIpoYear())
                .append(getSector())
                .append(getIndustry())
                .append(getSummaryQuote())
                .append(getDividendsInfo())
                .toHashCode();
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Double> getPrices() {
        return prices;
    }

    public void setPrices(List<Double> prices) {
        this.prices = prices;
    }

    public List<Double> getMarketCaps() {
        return marketCaps;
    }

    public void setMarketCaps(List<Double> marketCaps) {
        this.marketCaps = marketCaps;
    }

    public Integer getIpoYear() {
        return ipoYear;
    }

    public void setIpoYear(Integer ipoYear) {
        this.ipoYear = ipoYear;
    }

    public Sector getSector() {
        return sector;
    }

    public void setSector(Sector sector) {
        this.sector = sector;
    }

    public Industry getIndustry() {
        return industry;
    }

    public void setIndustry(Industry industry) {
        this.industry = industry;
    }

    public String getSummaryQuote() {
        return summaryQuote;
    }

    public void setSummaryQuote(String summaryQuote) {
        this.summaryQuote = summaryQuote;
    }

    public DividendsInfo getDividendsInfo() {
        return dividendsInfo;
    }

    public void setDividendsInfo(DividendsInfo dividendsInfo) {
        this.dividendsInfo = dividendsInfo;
    }
}
