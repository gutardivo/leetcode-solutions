export function romanToInt(s: string): number {
    const values: { [key: string]: number } = {
        "I": 1, "V": 5,
        "X": 10, "L": 50,
        "C": 100, "D": 500,
        "M": 1000, "IV": 4,
        "IX": 9, "XL": 40,
        "XC": 90, "CD": 400,
        "CM": 900
    }

    const sum = { value: 0 }
    

    for (let i=0;i<s.length;i++) {
        const letter = s[i]
        const nextLetter = s[i+1]
        
        if (values[letter] < values[nextLetter]) {
            const subLetter = letter+nextLetter
            const valueNew = values[subLetter]
            i++

            sum.value += valueNew
        } else {
            sum.value += values[letter]
        }
    }
    
    return sum.value
};
