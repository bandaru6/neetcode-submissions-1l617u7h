class ListNode {
    public:
        int val;
        ListNode* prev;
        ListNode* next;
        ListNode(int v, ListNode* pre = nullptr, ListNode* nxt = nullptr) : val(v), prev(pre), next(nxt) {}
};

class MyCircularQueue {
private:
    int space;
    ListNode* left;
    ListNode* right;
public:
    MyCircularQueue(int k) {
        this->space = k;
        this->left = new ListNode(0, nullptr, nullptr);
        this->right = new ListNode(0, this->left, nullptr);
        this->left->next = this->right;
    }
    
    bool enQueue(int value) {
        if (this->isFull()) {
            return false;
        }
        ListNode* curr = new ListNode(value, this->right->prev, this->right);
        this->right->prev->next = curr;
        this->right->prev = curr;
        this->space -= 1;
        return true;
    }
    
    bool deQueue() {
        if (this->isEmpty()) {
            return false;
        }
        ListNode* temp = this->left->next;
        this->left->next = this->left->next->next;
        this->left->next->prev = this->left;
        this->space += 1;
        delete temp;
        return true;
    }
    
    int Front() {
        if (this->isEmpty()) {
            return -1;
        }
        return this->left->next->val;
    }
    
    int Rear() {
        if (this->isEmpty()) {
            return -1;
        }
        return this->right->prev->val;
    }
    
    bool isEmpty() {
        return this->left->next == this->right;
    }
    
    bool isFull() {
        return this->space == 0;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */