import { convert } from "./6-zigzag-conversion";

describe("Zigzag Conversion", () => {
    test("Example 1: PAYPALISHIRING with numRows = 3", () => {
        expect(convert("PAYPALISHIRING", 3)).toBe("PAHNAPLSIIGYIR");
    });

    test("Example 2: PAYPALISHIRING with numRows = 4", () => {
        expect(convert("PAYPALISHIRING", 4)).toBe("PINALSIGYAHRPI");
    });

    test("Single character input", () => {
        expect(convert("A", 1)).toBe("A");
    });
});

