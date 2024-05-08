import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class Translator {
	private static final boolean DEBUG_MODE = false;

	public static void main(String[] args) {
		String[] elements;
		try {
			elements = readElements();
		} catch(FileNotFoundException e) {
			System.out.println(e);
			return;
		}

		Scanner scanner = new Scanner(System.in);
		String[] inputs;
		if(!DEBUG_MODE) {
			System.out.print("Enter word or list of words delimited by spaces: ");
			String i = scanner.nextLine();
			inputs = i.split(" ");
		} else {
			inputs = new String[] { "thermodynamics" };
		}

		for (String input: inputs) {
			// Skip word if empty.
			// This happens if user puts 2+ spaces between words.
			if(input.length() == 0) {
				continue;
			}
			Word word = convert("0" + input + "0", elements);
			log("*********************************************\n");
			transform(word);
			log("*********************************************\n");
			System.out.println(word.prettify());
		}

		scanner.close();
	}
	private static String[] readElements() throws FileNotFoundException {
		Scanner file = new Scanner(new File("elements.csv"));
		String output = file.nextLine();
		file.close();
		return output.split(",");
	}
	private static Word convert(String word, String[] elements) {
		Word output = new Word();
		int index;
		String str;

		for(int i = 1; i < word.length() - 1; i++) {
			// Check current
			str = "" + word.charAt(i) + "_";
			log("Checking if " + str + " is a valid symbol...");
			index = Arrays.binarySearch(elements, str);
			if(index >= 0) {
				log("yes\n");
				output.append(elements[index]);
			} else {
				log("no\n");
				output.appendEmpty(word.charAt(i));
			}

			// Check next
			str = "" + word.charAt(i) + word.charAt(i + 1);
			log("Checking if " + str + " is a valid symbol...");
			index = Arrays.binarySearch(elements, str);
			if(index >= 0) {
				log("yes\n");
				output.append(str);
			} else {
				log("no\n");
				output.appendEmpty();
			}
			log("Output is now: " + output + "\n");
		}

		return output;
	}
	private static void transform(Word word) {
		Window slice;
		while(word.hasNext()) {
			slice = word.next();
			log("Checking slice: " + slice +  " = " + slice.toBitFormat() + "\n");
			switch(slice.toBitFormat()) {
				case 4:
				case 6:
					log("Set prev\n");
					word.setPrev();
					break;
				case 2:
					log("Set mid\n");
					word.setMid();
					break;
				case 1:
					log("Set next\n");
					word.setNext();
					break;
				case 3:
					if(word.hasNext() && word.peek().NEXT.isValid()) 
						word.chainBreak();
					else {
						log("Set next\n");
						word.setNext();
					}
			}
			log("Word is now " + word + "\n");
		}
	}

	// Helper method for displaying debug logs.
	public static void log(String msg) {
		if(DEBUG_MODE) {
			System.out.print(msg);
		}
	}
}
