function selectionSort(inputArray){
    const n = inputArray.length;
    for(let i = 0; i<n; i++){
        let min = i;
        for(let j = i+1; j<n; j++){
            if(inputArray[j] < inputArray[min] ){
                min = j
            }
        }
        if(min != i){
            let temp = inputArray[i];
            inputArray[i] = inputArray[min];
            inputArray[min]= temp;
        }
    }
    return inputArray;
}

let array = [5, 2, 4, 6, 1, 3];
selectionSort(array);
console.log(array);

