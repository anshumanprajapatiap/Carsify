console.log('hello after codes')

const carDataBox = document.getElementById('companyname-99a6d115-5e68-4355-a7d0-529207feb0b3_2983')
const carInput = document.getElementById('companyname-99a6d115-5e68-4355-a7d0-529207feb0b3_2983')

const modelsDataBox = document.getElementById('modelname-99a6d115-5e68-4355-a7d0-529207feb0b3_2983')
const modelInput = document.getElementById('modelname-99a6d115-5e68-4355-a7d0-529207feb0b3_2983')

const modelText = document.getElementById('model-text')


$.ajax({
    type: 'GET',
    url: '/cars-json',
    success: function(response){
        console.log(response.data)
        const carsData = response.data
        carsData.map(item=>{
            //<option value="{{car_id}}" >{{car}}</option>
            const option = document.createElement('option')
            option.textContent = item.Car_Company_Name
            option.setAttribute('value', item.id)
            option.setAttribute('class', 'caritem')
            
            option.setAttribute('data-value', item.id)
            carDataBox.appendChild(option)
        })
    },
    error: function(error){
        console.log(error)
    }
});


carInput.addEventListener('change', e=>{
    console.log(e.target.value)
    const selectedCar = e.target.value

    modelsDataBox.innerHTML = ""
    modelText.textContent = "-- select an option --"
    modelText.classList.add("default-model")

    $.ajax({
        type: 'GET',
        url: `models-json/${selectedCar}`,
        success: function(response){
            console.log(response.data)
            const modelsData = response.data
            modelsData.map(item=>{
                const option = document.createElement('option')
                option.textContent = item.Car_Model_Name
                option.setAttribute('class', 'modelitem')
                option.setAttribute('data-value', item.id)
                option.setAttribute('value', item.id)
                modelsDataBox.appendChild(option)
            })
        },
        error: function(error){
            console.log(error)
        }
    })
})