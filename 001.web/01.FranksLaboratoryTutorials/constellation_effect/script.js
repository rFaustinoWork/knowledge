const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const particlesArray = [];
let hue = 0;

window.addEventListener('resize', function(){
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
});


const mouse = {
    x: undefined,
    y: undefined,
}
canvas.addEventListener('click', function(event){
    mouse.x = event.x;
    mouse.y = event.y;
    init();
});

canvas.addEventListener('mousemove', function(event){
    mouse.x = event.x;
    mouse.y = event.y;
    init();
});

class Particle{
    constructor(){
        this.x = mouse.x;
        this.y = mouse.y;
        this.size = Math.random() * 15 + 1;
        this.speedX = Math.random() * 5 - 1.5;
        this.speedY = Math.random() * 5 - 1.5;
        this.color = 'hsl('+hue+',100%, 50%)';
    }
    update(timestamp){
        this.x += this.speedX;
        this.y += this.speedY;
        if( this.size > 0.2) this.size -= 0.1;
    }
    draw(context){
        context.fillStyle = this.color;
        context.beginPath();
        context.arc(this.x, this.y, this.size, 0, Math.PI*2);
        context.fill();
    }
}


function init(){
    for(let i = 0; i < 2 ; i++){
        particlesArray.push(new Particle());
    }
}
// init();

function handleParticles(timestamp){
    for(let i = 0; i < particlesArray.length; i++){
        particlesArray[i].update(timestamp);
        particlesArray[i].draw(ctx);
        
        for(let j = i ; j < particlesArray.length; j++){
            const dx = particlesArray[i].x - particlesArray[j].x;
            const dy = particlesArray[i].y - particlesArray[j].y;
            const dist = Math.sqrt(dx*dx + dy*dy);

            if( dist < 100){
                ctx.beginPath();
                ctx.strokeStyle = particlesArray[i].color;
                ctx.lineWidth = particlesArray[i].size/10;
                ctx.moveTo(particlesArray[i].x, particlesArray[i].y);
                ctx.lineTo(particlesArray[j].x, particlesArray[j].y);
                ctx.stroke();
                ctx.closePath();
            }
        }
        
        if( particlesArray.size < 0.3){
            particlesArray.splice(i, 1);
            i--;
        }
    }
}

function animate(timestamp){
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    handleParticles(timestamp);
    hue+=5;
    requestAnimationFrame(animate);
}

animate(0);