let currentIndex = 0;

function changeSlide(direction) {
    const slides = document.getElementById('slider');
    const totalSlides = slides.children.length;

    currentIndex = (currentIndex + direction + totalSlides) % totalSlides;

    const transformValue = -currentIndex * 100 + '%';
    slides.style.transform = 'translateX(' + transformValue + ')';
}
