

button.addEventListener('click', async ()=> {
    let data = ["calc.py", input.value];
    // window.api.send("toMain", data);
    const newData = await window.api.invoke("toMain", data);
    result.textContent = newData;
});

// 
button.dispatchEvent(new Event('click'));

