function groupAnagrams(strs) {
    const groups = new Map();

    for (const s of strs) {
        let key = new Array(26).fill(0);

        for (const c of s) {
            key[c.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        }

        const keyStr = key.join(','); // Convert array to a string key

        if (!groups.has(keyStr)) {
            groups.set(keyStr, []);
        }

        groups.get(keyStr).push(s);
    }

    return Array.from(groups.values());
}

// Example usage:
const words = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(groupAnagrams(words));

