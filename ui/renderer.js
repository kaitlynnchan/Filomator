
const windowApi = window.api;

button.addEventListener('click', async ()=> {
    let data = windowApi.packageData("calc.py", input.value);
    // window.api.send("toMain", data);
    await windowApi.invoke("toMain", data).then(receivedData => {
        result.textContent = receivedData;
    });
});

button.dispatchEvent(new Event('click'));

