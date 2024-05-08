public class Window {
	public final Symbol PREV;
	public final Symbol CURR;
	public final Symbol NEXT;

	public Window(Symbol prev, Symbol curr, Symbol next) {
		PREV = prev;
		CURR = curr;
		NEXT = next;
	}

	public int toBitFormat() {
		return 4 * (PREV.isValid() ? 1 : 0)
			+ 2 * (CURR.isValid() ? 1 : 0)
			+ 1 * (NEXT.isValid() ? 1 : 0);
	}
	
	@Override
	public String toString() {
		return "(" + PREV + "," + CURR + "," + NEXT + ")";
	}
}
