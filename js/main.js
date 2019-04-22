$(document).ready(function(){
   jQuery.fn.makeItBounce = function(){
     
     //Let's do some style
     this.width(900).height(300).css('background-color', '#000');
     
     for(var i=0; i<140;i++){
       //Let's add something
       this.append('<ball></ball>');
       var ball = this.find('ball').eq(0);
       ball.width(30).height(30).css('background-color', '#fff').css('display','inline-block').css('border-radius','15px').css('position','absolute').css('top',285);

       var x,y,affX,affY;
       var initX = parseInt(ball.css('left'));
       var initY = parseInt(ball.css('top'));

       var rdX = Math.floor(Math.random() * 20) + 15; 
       var rdY = Math.floor(Math.random() * 100) + 200;

       for (x = 1 ; x < 28; x = x+.2){
         y = (Math.abs(Math.sin(x)))/x;
         affX = initX + x * rdX;
         affY = initY - y * rdY;
         ball.animate({left: affX, top: affY},10);
       }      
     }
   }
  
   $('div.area').makeItBounce();
   
});