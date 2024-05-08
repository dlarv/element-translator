public class Symbol {
	final String EMPTY = "00";
	String value;

	public Symbol() {
		value = "00";
	}

	public Symbol(String value) {
		this.value = value;
	}

	public void clear() {
		this.value = EMPTY;
	}

	public boolean isValid() {
		return value != "00" && !value.contains("*");
	}
	@Override
	public String toString() {
		return value;
	}
	public String prettify() {
		if(value.equals(EMPTY)) 
			return "";

		if(isValid()) 
			return value.substring(0, 1).toUpperCase() + value.substring(1).replace("_", "");
		return value.replace("*", "");
	}
}
