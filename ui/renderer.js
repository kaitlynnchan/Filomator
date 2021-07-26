

button.addEventListener('click', async ()=> {
    let data = ["calc.py", input.value];
    // window.api.send("toMain", data);
    await window.api.invoke("toMain", data).then(receivedData => {
        result.textContent = receivedData;
    });
});

button.dispatchEvent(new Event('click'));

