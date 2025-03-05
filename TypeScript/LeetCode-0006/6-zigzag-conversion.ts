export function convert(s: string, numRows: number): string {
    if (numRows === 1 || s.length <= numRows) return s;

    let result = "";
    const step = 2 * numRows - 2; // The cycle length

    for (let row = 0; row < numRows; row++) {
        for (let i = row; i < s.length; i += step) {
            result += s[i]; // Always add the first character in the row
            
            let diagonal = i + step - 2 * row;
            if (row > 0 && row < numRows - 1 && diagonal < s.length) {
                result += s[diagonal]; // Add the diagonal character
            }
        }
    }

    return result;
}
