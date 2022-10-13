const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

ctx.fillStyle = 'blue';
ctx.fillRect(200, 200, 150, 150);

// ctx.globalCompositeOperation = 'source-over';
// ctx.globalCompositeOperation = 'source-in';
// ctx.globalCompositeOperation = 'source-out';
// ctx.globalCompositeOperation = 'source-atop';
// ctx.globalCompositeOperation = 'destination-over';
// ctx.globalCompositeOperation = 'destination-int';
// ctx.globalCompositeOperation = 'destination-out';
// ctx.globalCompositeOperation = 'destination-atop';

// ctx.globalCompositeOperation = 'lighter';
// ctx.globalCompositeOperation = 'copy';
// ctx.globalCompositeOperation = 'xor';
// ctx.globalCompositeOperation = 'multiply';
// ctx.globalCompositeOperation = 'screen';
// ctx.globalCompositeOperation = 'overlay';
// ctx.globalCompositeOperation = 'darken';
// ctx.globalCompositeOperation = 'lighten';

// ctx.globalCompositeOperation = 'color-dodge';
// ctx.globalCompositeOperation = 'color-burn';

// ctx.globalCompositeOperation = 'hard-light';
// ctx.globalCompositeOperation = 'soft-light';

// ctx.globalCompositeOperation = 'difference';
// ctx.globalCompositeOperation = 'exclusion';
// ctx.globalCompositeOperation = 'hue';
// ctx.globalCompositeOperation = 'saturation';
// ctx.globalCompositeOperation = 'color';
ctx.globalCompositeOperation = 'luminosity';


ctx.fillStyle = 'red';
ctx.beginPath();
ctx.arc(350, 350, 75, 0, Math.PI * 2);
ctx.fill();

