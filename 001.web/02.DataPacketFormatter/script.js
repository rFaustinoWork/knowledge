

const canvas = document.getElementById("canvas1");
const textarea = document.getElementById("textarea1")

const ctx = canvas.getContext("2d");
canvas.width = 1000;
canvas.height = 600;



// function btn_save_click()
// {
//     var dataURL = canvas.toDataURL("image/png", 1.0);
//     var a = document.createElement('a');
//     a.href = dataURL;
//     a.download = 'packet.png';
//     a.click();
// }


function btn_generate_click()
{
    // alert(textarea.value)
    
    const json = textarea.value;
    const obj = JSON.parse(json);

    if(!obj.hasOwnProperty("style") ||
       !obj.hasOwnProperty("packets"))
    {
        alert("Invalid input script. Missing properties.")   
        return;
    }

    style = obj["style"]
    packets = obj["packets"]

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.beginPath();

    y_offset = 50
    for(var i = 0; i < packets.length; i++)
    {
        y_offset = paint_packet(style, packets[i], y_offset)
        y_offset += 50
    }
}

function paint_packet(style, packet_data, y_offset)
{
    byte_width = getPropertyValue(style, "byte_width", 15);
    stroke_style = getPropertyValue(style, "stroke_style", "gray");
    font_byte_nr = getPropertyValue(style, "font_byte_nr", "12px serif");
    font_field_name = getPropertyValue(style, "font_field_name", "12px serif");
    fill_byte_nr = getPropertyValue(style, "fill_byte_nr", "black");
    fill_field_name = getPropertyValue(style, "fill_field_name", "black");
    font_packet_name = getPropertyValue(style, "font_packet_name", "12px serif");
    fill_packet_name = getPropertyValue(style, "fill_packet_name", "black");

    x_offset = 150;

    // Compute the packet lenght
    nb_bytes = 0
    for(var i = 0; i < packet_data["bits"].length; i++)
    {
        length = packet_data["bits"][i]["length"]
        nb_bytes += length;
    }

    // Draw the packet outside boundaries
    ctx.strokeStyle = stroke_style
    ctx.rect(x_offset, y_offset, nb_bytes*byte_width, 30)
    ctx.stroke()

    level = 0
    last_level_x = 1000
    higher_level = 0
    
    // Draw packet name
    ctx.font = font_packet_name;
    ctx.fillStyle = fill_packet_name;
    txt_width = ctx.measureText(packet_data["name"]).width
    ctx.fillText(packet_data["name"], x_offset-txt_width-10, y_offset+20)

    // Draw the packet internal data (bytes)
    ctx.font = font_field_name;
    ctx.fillStyle = fill_field_name;
    for(var i = packet_data["bits"].length-1; i >= 0; i--)
    {
        first = packet_data["bits"][i]["first"]
        width = packet_data["bits"][i]["length"]
        text = packet_data["bits"][i]["name"]
        txt_width = ctx.measureText(text).width

        // force the length to be at least 1 byte
        if( width < 1) width = 1

        // draw the byte outside boundary
        ctx.rect(x_offset+first*byte_width, y_offset, width*byte_width, 30)
        ctx.stroke()
        
        // draw the byte name. The name is drawn inside the packet boundaries if it fits. 
        // Otherwise, the name is drawn below the packet. 
        if( txt_width < width*byte_width-5)
        {
            ctx.fillText(text, x_offset+2+first*byte_width, y_offset+20)
        }else
        {
            x = x_offset+5+first*byte_width
            // Checks whether the text hits another field text. If it does, it is drawn a level below
            if( x + txt_width >= last_level_x){
                level += 18;
            }else
            {
                level = 18;
            }
            ctx.fillText(text, x, y_offset+30+level)
            ctx.moveTo(153+first*byte_width, y_offset+30)
            ctx.lineTo(153+first*byte_width, y_offset+30+level-5)
            ctx.stroke()
            last_level_x = x
        }
        if( level > higher_level) higher_level = level;

    }

    // Draw the bytes label
    for(var i = 0; i < nb_bytes; i++)
    {
        ctx.fillStyle = fill_byte_nr
        ctx.font = font_byte_nr;
        ctx.fillText(i, x_offset+3+i*byte_width, y_offset-3)
    }

    // Draw the bytes boundary tick
    for(var i = 1; i < nb_bytes; i++)
    {
        ctx.moveTo(x_offset+i*byte_width, y_offset)
        ctx.lineTo(x_offset+i*byte_width, y_offset+5)
        ctx.stroke()
    }

    // Return the higher Y coordinate used in the drawing
    return higher_level+20+y_offset;
}

function getPropertyValue(style, property_name, value_if_not_defined)
{
    if(style.hasOwnProperty(property_name))
    {
        return style[property_name];
    }
    return value_if_not_defined;
}



//////////////////////////////////////////////////////////////////////////////////////////
// Code to disable default behaviour of tab key on textarea. With this code the tab
//  inserts a '\t' char in the textarea instead of moving focus to other element.
function insertAtCursor (el, text) {
    text = text || '';
    if (document.selection) {
      // IE
      el.focus();
      var sel = document.selection.createRange();
      sel.text = text;
    } else if (el.selectionStart || el.selectionStart === 0) {
      // Others
      var startPos = el.selectionStart;
      var endPos = el.selectionEnd;
      el.value = el.value.substring(0, startPos) +
        text +
        el.value.substring(endPos, el.value.length);
      el.selectionStart = startPos + text.length;
      el.selectionEnd = startPos + text.length;
    } else {
      el.value += text;
    }
};
  
document.querySelector("#textarea1").addEventListener("keydown", function(e) {
      var TABKEY = 9;
      if(e.keyCode == TABKEY) {
          insertAtCursor(this, "\t");
      if(e.preventDefault) {
          e.preventDefault();
      }
      return false;
      }
}, false);
///////////////////////////////////////////////////////////////////////////////////////// 