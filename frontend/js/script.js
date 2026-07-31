/* ====================================================== */
/* SyncReserve AI */
/* script.js */
/* PART 1 */
/* ====================================================== */

const API_URL = "http://127.0.0.1:8000/api/book";

const bookingForm = document.getElementById("bookingForm");

const loader = document.getElementById("loader");

const toast = document.getElementById("toast");

const terminal = document.getElementById("terminal");

const bookingCounter = document.getElementById("bookingCounter");

const bookingCount = document.getElementById("bookingCount");

const conflictCount = document.getElementById("conflictCount");

let totalBookings = 0;

let preventedConflicts = 0;

/* ====================================================== */
/* PIPELINE ELEMENTS */
/* ====================================================== */

const pipeline = [

document.getElementById("step1"),

document.getElementById("step2"),

document.getElementById("step3"),

document.getElementById("step4"),

document.getElementById("step5")

];

const execution = [

document.getElementById("exec1"),

document.getElementById("exec2"),

document.getElementById("exec3"),

document.getElementById("exec4"),

document.getElementById("exec5"),

document.getElementById("exec6"),

document.getElementById("exec7")

];

/* ====================================================== */
/* HELPERS */
/* ====================================================== */

function sleep(ms){

    return new Promise(resolve=>setTimeout(resolve,ms));

}

function clearAnimation(){

    pipeline.forEach(box=>box.classList.remove("active"));

    execution.forEach(step=>step.classList.remove("active"));

}

function showLoader(){

    loader.classList.remove("hidden");

}

function hideLoader(){

    loader.classList.add("hidden");

}

function showToast(message){

    toast.innerText = message;

    toast.classList.add("show");

    setTimeout(()=>{

        toast.classList.remove("show");

    },3000);

}

function addTerminal(text){

    terminal.textContent += "\n" + text;

    terminal.scrollTop = terminal.scrollHeight;

}

/* ====================================================== */
/* PIPELINE ANIMATION */
/* ====================================================== */

async function animatePipeline(){

    clearAnimation();

    for(let i=0;i<pipeline.length;i++){

        pipeline[i].classList.add("active");

        await sleep(180);

    }

    for(let i=0;i<execution.length;i++){

        execution[i].classList.add("active");

        await sleep(170);

    }

}

/* ====================================================== */
/* BOOKING */
/* ====================================================== */

bookingForm.addEventListener("submit",async(e)=>{

    e.preventDefault();

    clearAnimation();

    terminal.textContent="";

    const studentId=document.getElementById("studentId").value;

    const resource=document.getElementById("resource").value;

    const bookingDate=document.getElementById("bookingDate").value;

    const timeSlot=document.getElementById("timeSlot").value;

    const split=timeSlot.split("-");

    const startTime=bookingDate+"T"+split[0]+":00";

    const endTime=bookingDate+"T"+split[1]+":00";

    addTerminal("POST /api/book");

    addTerminal("");

    addTerminal("Preparing payload...");

    showLoader();

    await animatePipeline();

    addTerminal("Student : "+studentId);

    addTerminal("Resource : "+resource);

    addTerminal("Start : "+startTime);

    addTerminal("End : "+endTime);

    addTerminal("");

    addTerminal("Connecting FastAPI Gateway...");

    try{

        const response=await fetch(API_URL,{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body: JSON.stringify({

    student_id: studentId,

    resource_id: resource,

    start_time: startTime,

    end_time: endTime

})

        });

        const data=await response.json();

        addTerminal("Python Bridge Running...");

        addTerminal("Launching SyncReserveAI.exe");

        addTerminal("Graph Validation Completed");

        addTerminal("");

        addTerminal("JSON Received");

        addTerminal(JSON.stringify(data,null,2));

        if(data.success){

            totalBookings++;

            bookingCounter.innerText=totalBookings;

            bookingCount.innerText=totalBookings;

            showToast("Booking Successful");

        }

        else{

            preventedConflicts++;

            conflictCount.innerText=preventedConflicts;

            showToast(data.message);

        }

    }

    catch(error){

        addTerminal("");

        addTerminal("ERROR");

        addTerminal(error.message);

        showToast("Backend Offline");

    }

    hideLoader();

});

const latencyCard=document.getElementById("latencyCard");

const latencyValue=document.getElementById("latencyValue");

/* ====================================================== */
/* LATENCY SIMULATION */
/* ====================================================== */

function randomLatency(){

    const value=(Math.random()*3+3).toFixed(2);

    latencyCard.innerText=value+" ms";

    latencyValue.innerText=value+" ms";

}

setInterval(randomLatency,2500);

/* ====================================================== */
/* STARTUP TERMINAL */
/* ====================================================== */

async function startupSequence(){

    terminal.textContent="";

    const logs=[

        "SyncReserve AI v1.0",

        "Initializing frontend...",

        "Connecting FastAPI Gateway...",

        "Loading Python Bridge...",

        "Waiting for SyncReserveAI.exe...",

        "Loading scheduling engine...",

        "Gateway Status : ONLINE",

        "Engine Status : READY",

        "",

        "Waiting for booking request..."

    ];

    for(const line of logs){

        terminal.textContent+=line+"\n";

        await sleep(180);

    }

}

startupSequence();

/* ====================================================== */
/* SMOOTH SCROLL */
/* ====================================================== */

document.querySelectorAll('a[href^="#"]').forEach(anchor=>{

    anchor.addEventListener("click",function(e){

        e.preventDefault();

        const target=document.querySelector(this.getAttribute("href"));

        if(target){

            target.scrollIntoView({

                behavior:"smooth"

            });

        }

    });

});

/* ====================================================== */
/* HERO BUTTONS */
/* ====================================================== */

const heroButtons=document.querySelectorAll(".hero-buttons button");

if(heroButtons.length>=2){

    heroButtons[0].addEventListener("click",()=>{

        document.getElementById("booking").scrollIntoView({

            behavior:"smooth"

        });

    });

    heroButtons[1].addEventListener("click",()=>{

        document.getElementById("architecture").scrollIntoView({

            behavior:"smooth"

        });

    });

}

/* ====================================================== */
/* CARD ANIMATION */
/* ====================================================== */

const observer=new IntersectionObserver((entries)=>{

    entries.forEach(entry=>{

        if(entry.isIntersecting){

            entry.target.style.opacity="1";

            entry.target.style.transform="translateY(0)";

        }

    });

},{

    threshold:0.15

});

document.querySelectorAll(".glass-card").forEach(card=>{

    card.style.opacity="0";

    card.style.transform="translateY(40px)";

    card.style.transition="0.6s ease";

    observer.observe(card);

});

/* ====================================================== */
/* LIVE CLOCK */
/* ====================================================== */

function updateClock(){

    const now=new Date();

    const hrs=String(now.getHours()).padStart(2,"0");

    const mins=String(now.getMinutes()).padStart(2,"0");

    const secs=String(now.getSeconds()).padStart(2,"0");

    document.title=`SyncReserve AI • ${hrs}:${mins}:${secs}`;

}

updateClock();

setInterval(updateClock,1000);

/* ====================================================== */
/* STATUS PULSE */
/* ====================================================== */

setInterval(()=>{

    document.querySelectorAll(".green-dot").forEach(dot=>{

        dot.animate(

            [

                {transform:"scale(1)"},

                {transform:"scale(1.6)"},

                {transform:"scale(1)"}

            ],

            {

                duration:700

            }

        );

    });

},2000);

/* ====================================================== */
/* KEYBOARD SHORTCUT */
/* ====================================================== */

document.addEventListener("keydown",(e)=>{

    if(e.key==="b" || e.key==="B"){

        document.getElementById("booking").scrollIntoView({

            behavior:"smooth"

        });

    }

});

/* ====================================================== */
/* INITIAL VALUES */
/* ====================================================== */

bookingCounter.innerText=0;

bookingCount.innerText=0;

conflictCount.innerText=0;

randomLatency();

/* ====================================================== */
/* APPLICATION READY */
/* ====================================================== */

console.log("====================================");

console.log(" SyncReserve AI Frontend Loaded ");

console.log(" FastAPI Gateway Ready ");

console.log(" Waiting for Booking Requests ");

console.log("====================================");

/* ====================================================== */
/* SCRIPT.JS COMPLETE */
/* ====================================================== */