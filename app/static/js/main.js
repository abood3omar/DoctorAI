document.addEventListener('DOMContentLoaded', () => {

    const modelSelect = document.getElementById('modelSelect');
    const fileInput = document.getElementById('fileInput');
    const imagePreview = document.getElementById('imagePreview');
    const previewText = document.getElementById('previewText');
    const predictButton = document.getElementById('predictButton');
    
    const resultContainer = document.getElementById('resultContainer');
    const resultElement = document.getElementById('result');
    const loadingElement = document.getElementById('loading');
    
    let selectedFile = null;

    fileInput.addEventListener('change', (event) => {
        selectedFile = event.target.files[0];
        if (selectedFile) {
            const reader = new FileReader();
            reader.onload = (e) => {
                imagePreview.src = e.target.result;
                imagePreview.classList.remove('hidden');
                previewText.classList.add('hidden');
            };
            reader.readAsDataURL(selectedFile);
            hideResult();
        }
    });

    predictButton.addEventListener('click', async () => {
        if (!selectedFile) {
            alert('الرجاء اختيار صورة أولاً.');
            return;
        }

        const selectedModel = modelSelect.value;
        const API_URL = `/api/predict/${selectedModel}`;

        showLoading();

        const formData = new FormData();
        formData.append('file', selectedFile);

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                body: formData,
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `Error ${response.status}`);
            }

            const data = await response.json();
            displayResult(data);

        } catch (error) {
            console.error('Error during prediction:', error);
            displayError(error.message);
        }
    });
    
    function showLoading() {
        resultContainer.classList.remove('opacity-0', 'scale-95');
        resultElement.innerHTML = '';
        loadingElement.classList.remove('hidden');
    }

    function hideResult() {
        resultContainer.classList.add('opacity-0', 'scale-95');
        loadingElement.classList.add('hidden');
        resultElement.innerHTML = '';
    }

function displayResult(data) {
        let prediction = data.prediction.toLowerCase();
        let colorClass = 'text-white'; 

        // 1. الحالات الخطرة (أحمر)
        if (prediction.includes('malignant') || 
            prediction.includes('pneumonia') || 
            prediction.includes('tumor') || 
            prediction.includes('tuberculosis') ||
            prediction.includes('cavity') ||       
            prediction.includes('impacted') ||     
            prediction.includes('not visible') ||
            prediction.includes('mel') || 
            prediction.includes('bcc') || 
            prediction.includes('akiec') ||
            // (جديد - العدوى)
            prediction.includes('infected') && !prediction.includes('non')) { // نستخدم شرط !non عشان ما يلخبط مع noninfected
            
            colorClass = 'text-red-400';
        
        // 2. الحالات المتوسطة (أصفر)
        } else if (prediction.includes('benign') || 
                   prediction.includes('filling') || 
                   prediction.includes('implant') ||
                   prediction.includes('vasc') ||
                   prediction.includes('df')) {
            
            colorClass = 'text-yellow-400';

        // 3. الحالات السليمة (أخضر)
        } else if (prediction.includes('normal') || 
                   prediction.includes('visible') ||
                   prediction.includes('nv') || 
                   prediction.includes('bkl') ||
                   // (جديد - غير مصاب)
                   prediction.includes('noninfected')) {
            
            colorClass = 'text-green-400';
        }

        loadingElement.classList.add('hidden');
        resultElement.innerHTML = `
            <h3 class="font-bold text-3xl ${colorClass}">
                ${data.prediction}
            </h3>
          
        `;
    }
    function displayError(errorMessage) {
        loadingElement.classList.add('hidden');
        resultElement.innerHTML = `
            <h3 class="font-bold text-2xl text-red-400">
                حدث خطأ
            </h3>
            <p class="text-gray-300 mt-2 text-sm">${errorMessage}</p>
        `;
    }
});