const tooltip = document.getElementById('tooltip');

document.querySelectorAll('svg a').forEach(area => {
    area.addEventListener('mousemove', (e) => {
        tooltip.innerHTML = area.dataset.info;
        tooltip.style.opacity = 1;
        tooltip.style.left = (e.pageX + 10) + 'px';
        tooltip.style.top = (e.pageY + 10) + 'px';
    });

    area.addEventListener('mouseleave', () => {
        tooltip.style.opacity = 0;
    });
});
