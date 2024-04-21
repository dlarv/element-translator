#!/bin/bash 

file="import unittest
from translator import main as execute


class TestTranslator(unittest.TestCase):
"

# (Re)Create file 
echo "$file" > '_test.py'

while read line; do
	IFS=';' read -ra ARR <<< "$line"
	func="    def test_${ARR[0]}(self):
        output = execute(['-t', '${ARR[1]}'])[0]
        self.assertIs(int(output[0]), int(${ARR[2]}), f\"Expected: ${ARR[3]}. Actual: {output[1]}.\")
"
	echo "$func" >> '_test.py'
done <"../../testing/solutions.txt"

echo "if __name__ == '__main__':
    unittest.main()" >> '_test.py'
