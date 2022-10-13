const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;


let particlesArray;

let mouse = {
    x: null,
    y: null,
    radius: (canvas.height/80) * (canvas.width/80)
}
    
window.addEventListener("mousemove", 
    function(event)
    {
        mouse.x = event.x;
        mouse.y = event.y;
    }
);

window.addEventListener("mouseout", 
    function(event)
    {
        mouse.x = undefined;
        mouse.y = undefined;
    }
);

window.addEventListener("resize", 
    function(){
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        mouse.radius = (canvas.height/80) * (canvas.width/80);
        init();
    }
);

class Particle{
    constructor(x, y, directionX, directionY, size, color)
    {
        this.x = x;
        this.y = y;
        this.directionX = directionX;
        this.directionY = directionY;
        this.size = size;
        this.color = color;
    }

    draw(){
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fillStyle = this.color;
        ctx.fill();
    }

    update()
    {
        if(this.x > canvas.width || this.x < 0){
            this.directionX = -this.directionX;
        }
        if(this.y > canvas.height || this.y < 0){
            this.directionY = -this.directionY;
        }

        let dx = mouse.x - this.x;
        let dy = mouse.y - this.y;
        let dist = Math.sqrt(dx*dx + dy*dy);
        if(dist < mouse.radius + this.size){
            if(mouse.x < this.x && this.x < canvas.width - this.size * 10){
                this.x += 10;
            }
            if(mouse.x > this.x & this.x > this.size * 10){
                this.x -= 10;
            }
            if(mouse.y < this.y && this.y < canvas.height - this.size * 10){
                this.y += 10;
            }
            if(mouse.y > this.y & this.y > this.size * 10){
                this.y -= 10;
            }
        }
        this.x += this.directionX;
        this.y += this.directionY;
        this.draw();
    }
}

function init()
{
    particlesArray = [];
    let numberOfParticles = (canvas.width * canvas.height) / 5000;
    for(let i = 0; i < numberOfParticles; i++)
    {
        let size = Math.random() * 5 + 1;
        let x = (Math.random() * ((window.innerWidth - size * 2) - (size * 2)) + size * 2)
        let y = (Math.random() * ((window.innerHeight - size * 2) - (size * 2)) + size * 2)
        let directionX = (Math.random() * 5) - 2.5;
        let directionY = (Math.random() * 5) - 2.5;
        let color = '#8c5532';
        
        particlesArray.push(new Particle(x, y, directionX, directionY, size, color));
    }
}

function animate(){
    requestAnimationFrame(animate);
    ctx.clearRect(0, 0, window.innerWidth, window.innerHeight);
    for(let i = 0; i < particlesArray.length; i++){
        particlesArray[i].update();
    }
    connect();
}

function connect(){
    let opacityValue = 1;
    for(let a = 0; a < particlesArray.length; a++){
        for(let b = 0; b < particlesArray.length; b++){
            let difX = (particlesArray[a].x - particlesArray[b].x);
            let difY = (particlesArray[a].y - particlesArray[b].y);
            let dist = (difX * difX) + (difY * difY);
            if( dist < (canvas.width/7) * (canvas.height/7)){
                opacityValue = 1 - (dist / 20000);
                ctx.strokeStyle = 'rgba(140, 85, 31, '+opacityValue+')';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.moveTo(particlesArray[a].x, particlesArray[a].y);
                ctx.lineTo(particlesArray[b].x, particlesArray[b].y);
                ctx.stroke();
            }

        }
    }
}


init();
animate();

