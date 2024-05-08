import java.util.ArrayList;

public class Word {
	ArrayList<Symbol> letters;
	int index;

	public Word() {
		letters = new ArrayList<>();
		letters.add(new Symbol());
		// +2 inside of next()
		index = -1;
	}

	public void append(String val) {
		letters.add(new Symbol(val));
	}
	public void appendEmpty() {
		letters.add(new Symbol());
	}
	public void appendEmpty(char val) {
		letters.add(new Symbol("" + val + "*"));
	}
	public boolean hasNext() {
		return index < letters.size() - 3;
	}
	public Window next() {
		index += 2;
		Symbol prev, curr, next;

		prev = letters.get(index - 1);
		curr = letters.get(index); 
		next = letters.get(index + 1);

		return new Window(prev, curr, next);
	}
	public Window peek() {
		if(!hasNext()) {
			throw new IndexOutOfBoundsException();
		}
		int initial = index;
		Window win = next();
		index = initial;
		return win;
	}

	public void setPrev() { for(int i = Math.max(index - 3, 0); i < index + 1; i++) {
			if(i == index - 1)
				continue;

			letters.get(i).clear();
		}
	}
	public void setMid() {
		letters.get(index - 1).clear();
		letters.get(index + 1).clear();
	}
	public void setNext() {
		int end = Math.min(index + 3, letters.size() - 1);

		for(int i = index - 1; i < end; i++) {
			if(i == index + 1)
				continue;

			letters.get(i).clear();
		}
	}
	public void chainBreak() {
		int initial = index - 2;
		while(hasNext()) {
			Window win = next();
			if(!win.NEXT.isValid()) {
				setPrev();
				break;
			}
		}
		index = initial;
	}
	@Override
	public String toString() {
		return letters.toString();
	}
	public String prettify() {
		StringBuilder str = new StringBuilder();
		String curr;

		for(Symbol sym: letters) {
			curr = sym.prettify();
			if(curr.length() > 0) {
				str.append(curr + ", ");
			}
		}
		// Remove last ", " and return
		return str.toString().substring(0, str.length() - 2);
	}
}
