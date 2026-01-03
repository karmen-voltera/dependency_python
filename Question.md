You are designing the software equivalent of a warehouse dispatch desk.

Packages arrive at the desk and must be sent out of the building.

The desk does **not** control or care how the package leaves. Think about what this means.

Packages may leave via:

* a conveyor belt  
* a forklift  
* a robotic arm  
* a loading dock pickup  
* or any future mechanism not yet designed

Your task \- if you chose to accept it \- is to design the system so that the dispatch desk works unchanged, regardless of how packages physically exit the warehouse.

## **Requirements**

### **1\. Exit Mechanism Interface**

Define an interface that represents any way a package can leave the warehouse.

* The interface must describe *what* happens, not *how*   
  * (Analogy, bowling, you have to knock pins down, imagine no one tells you how to do it. A bat? A ball? Rolling yourself into them? As long as they fall it’s fine)  
* Dispatching a package may succeed or fail  
* Failures must be communicated via exceptions (Not a hard requirement, but best practice)

### **2\. Concrete Exit Mechanisms**

Create at least two (of the above 5\) different exit mechanisms that represent realistic physical constraints.

Examples:

* weight limits  
* missing package information  
* mechanical limitations

Each mechanism must:

* implement the interface  
* contain no business logic unrelated to physically moving a package (super important)  
* be swappable without modifying the dispatch desk (this is the magic)

### **3\. Dispatch Desk (Business Logic)**

Create a dispatch desk that:

* accepts an exit mechanism via its constructor  
* validates incoming package data  
* hands the package off to the exit mechanism

Rules:

* The dispatch desk must not instantiate exit mechanisms  
* No conditional logic based on exit mechanism type  
* The dispatch desk must not change when new exit mechanisms are added (also magic)

### **4\. Unit Testing** 

You must write unit tests for the dispatch desk.

Constraints:

* Tests must not use real exit mechanisms  
* Tests must verify correct package construction  
* Tests must verify that dispatch occurs exactly once  
* Tests must verify failure behavior

### **5\. Failure Scenarios**

Your tests must cover:

* invalid package data  
* failures raised by the exit mechanism(s) you decided to implement. Try you best to handle/propagate these correctly.

