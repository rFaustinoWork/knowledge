

const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");
canvas.width = 400;
canvas.height = 600;
   

ctx.clearRect(0, 0, innerWidth, innerHeight);

ctx.beginPath();
// ctx.arc(100, 100, 10, 0, Math.PI*2, false);
// // ctx.fillRect(this.x, this.y, this.size, this.size);
ctx.fillStyle = "rgba(250, 0, 0, 0.8)";
// ctx.fill();
// ctx.strokeStyle = 'rgba(20,20,20,0.5)';
// ctx.stroke();
// ctx.closePath();

ctx.save()

ctx.translate(200, 300);

for(var i = 0; i < 8; i++)
{
    
    ctx.fillRect(50, 0, 10, 2);
    ctx.fillText("20", 50, -3)
    ctx.strokeStyle = 'rgba(20,20,20,0.5)';
    ctx.stroke();
    ctx.rotate(Math.PI/4);
}


ctx.restore()

