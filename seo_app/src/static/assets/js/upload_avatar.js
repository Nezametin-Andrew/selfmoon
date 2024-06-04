// Получаем ссылки на элементы DOM
var blImage = document.getElementById('wrapper_copper');
var imgElement = document.getElementById('copp_img');

// Присоединяем обработчик события к кнопке закрытия
var blClose = document.getElementById('closeBtnwind').addEventListener('click', function () {
    blImage.style.display = 'none'; // Устанавливаем стиль display: none для блока с изображением
    document.getElementById("avatar-upload").value = "";
    imgElement.setAttribute('src', '');
});

// Устанавливаем изначально стиль display: none для блока с изображением
blImage.style.display = 'none';

// Функция для изменения размеров изображения
function getImageResizing() {

    return  // Возвращаем обрезанное изображение в формате JPEG
}

// Обработчик события изменения выбранного файла
document.getElementById("avatar-upload").addEventListener("change", function () {
    console.log("Файл выбран:", this.files[0]);
    var file = this.files[0];
    var formData = new FormData();
    formData.append('avatar', file);
    var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    formData.append('csrfmiddlewaretoken', csrfToken);

    fetch(resiezeAvatarUrl, {
        method: 'POST',
        body: formData,
        meth: "resize",
    }).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            console.error("Ошибка при загрузке файла");
        }
    }).then(data => {
        console.log(baseUrl + data.image_path)
        // Отображаем блок с изображением
        blImage.style.display = 'block';
        // Устанавливаем источник изображения
        imgElement.setAttribute('src', baseUrl + data.image_path);

        // Получаем обрезанное изображение
        const image = document.getElementById('copp_img');
        const cropper = new Cropper(image, {
            aspectRatio: 1,
            viewMode: 1,
            zoomable: false,
            scalable: false,
            cropBoxResizable: false,
            minCropBoxWidth: 350,
            minCropBoxHeight: 350,
            maxCropBoxWidth: 350,
            maxCropBoxHeight: 350,
            background: false,
            modal: true,
            wheelZoomRatio: 0.01
        });  

      
        var croppedImage;

        document.getElementById('cropImageBtn').addEventListener('click', function(){
          croppedImage = cropper.getCroppedCanvas().toDataURL("image/jpeg");
          
          // Создаем FormData для отправки на сервер
          var formData = new FormData();
          formData.append('avatar', croppedImage);
          formData.append('csrfmiddlewaretoken', csrfToken);



          // Отправляем обрезанное изображение на сервер
            fetch(saveAvatarUrl, {
              method: 'POST',
              body: formData,
              meth: "save",
          }).then(response => {
              if (response.ok) {
                  console.log("Изображение успешно отправлено на сервер");

                  window.location.href = redirectUrl; // Перенаправляем пользователя
              } else {
                  console.error("Ошибка при отправке изображения на сервер");
              }
          }).catch(error => {
              console.error("Ошибка:", error);
          });
      }).catch(error => {
          console.error("Ошибка:", error);
      });
        })

       

        
});


