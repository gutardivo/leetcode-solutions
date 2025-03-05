import { addTwoNumbers, ListNode } from "./2-add-two-numbers";

function createLinkedList(arr: number[]): ListNode | null {
    let dummy = new ListNode(0);
    let current = dummy;
    for (const num of arr) {
        current.next = new ListNode(num);
        current = current.next;
    }
    return dummy.next;
}

function linkedListToArray(node: ListNode | null): number[] {
    const result: number[] = [];
    while (node) {
        result.push(node.val);
        node = node.next;
    }
    return result;
}

describe("addTwoNumbers", () => {
    test("Example 1", () => {
        const l1 = createLinkedList([2, 4, 3]);
        const l2 = createLinkedList([5, 6, 4]);
        const result = addTwoNumbers(l1, l2);
        expect(linkedListToArray(result)).toEqual([7, 0, 8]);
    });

    test("Example 2", () => {
        const l1 = createLinkedList([0]);
        const l2 = createLinkedList([0]);
        const result = addTwoNumbers(l1, l2);
        expect(linkedListToArray(result)).toEqual([0]);
    });

    test("Example 3", () => {
        const l1 = createLinkedList([9, 9, 9, 9, 9, 9, 9]);
        const l2 = createLinkedList([9, 9, 9, 9]);
        const result = addTwoNumbers(l1, l2);
        expect(linkedListToArray(result)).toEqual([8, 9, 9, 9, 0, 0, 0, 1]);
    });
});
