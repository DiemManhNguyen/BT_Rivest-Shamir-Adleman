document.addEventListener('DOMContentLoaded', function() {
    // Hiển thị tên file khi chọn
    const fileInputs = document.querySelectorAll('.file-input');
    
    fileInputs.forEach(input => {
        input.addEventListener('change', function() {
            const label = this.nextElementSibling;
            const fileName = this.files[0]?.name || 'Chọn file để tải lên';
            
            if (this.files[0]) {
                label.innerHTML = `<i class="fas fa-file"></i><span>${fileName}</span>`;
                label.style.justifyContent = 'flex-start';
                label.style.padding = '15px 20px';
                label.style.flexDirection = 'row';
                label.style.gap = '10px';
                label.style.alignItems = 'center';
            }
        });
    });
    
    // Hiệu ứng cho các nút
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
        button.addEventListener('mousedown', function() {
            this.style.transform = 'scale(0.98)';
        });
        
        button.addEventListener('mouseup', function() {
            this.style.transform = 'scale(1)';
        });
        
        button.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    });
});