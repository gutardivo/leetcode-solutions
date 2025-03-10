import { romanToInt } from "./13-roman-to-integer";

describe("romanToInt", () => {
    test("Example 1", () => {
        expect(romanToInt("III")).toBe(3);
    });

    test("Example 2", () => {
        expect(romanToInt("LVIII")).toBe(58);
    });

    test("Example 3", () => {
        expect(romanToInt("MCMXCIV")).toBe(1994);
    });
});
