// fn main() {
//     println!(" ");
//     println!("Hai bebi");
//     println!(" ");
    
// }

// fn main() {
//     println!("{}", 21 + 40);
    
// }

// difference between using print! and println!

// fn main() {
//     print!("Hello");
//     print!("World");
// }

// fn main() {
//     println!("Hello");
//     println!("World");
// }

// fn main() {
//     println!("{}", 3+4);
//     println!("{}", 2+1);
// }

// fn main() {
//     print!("{}",3+4);
//     println!("{}",2+1);
// }

// fn main(){
//     println!("{}",3+4);
//     print!("{}",2+1);
// }

// fn main() {
//     let length = 11;
//     let width = 13;

//     let area = length * width;
//     let perimeter = 2 * (length + width);

//     println!("{}", area);
//     println!("{}", perimeter); 
// }

// fn main() {
//     print!("{}\n{}",3+4,2+1);
// }

// fn main() {
//     print!("{} {} {}", 3+4, "", 2+1);

// }

// fn main() {
//     print!("{} {} {}", 3+4, "and", 2+1);
// }

// fn main() {
//     let first_result = 8 * 9;
//     let second_result = 2 * (100+200);

//     println!("{}", first_result);
//     print!("{}", second_result);
// }

// fn main() {
//     println!("{}",9-2);
//     print!("{}", 30/5);
// }

// fn main() {
//     let length = 13;
//     let mut width = 13;

//     // Calculate and print the area and perimeter
//     println!("{}", "This is the Old Stats");
//     println!("{}", length * width);
//     println!("{}", 2 * (length + width));
//     println!("{}","");

//     // Update the width 
//     width = 15; // replace the underscore with the correct value

//     // Calculate and print the new area and perimeter
//     println!("{}", "This is the New Stats");
//     println!("{}", length * width);
//     println!("{}", 2 * (length + width));
// }

// fn main() {
//     let number:i32 = 10;
//     println!("{}", number);

// }

// fn main() {
//     let a: i32 = 23;
//     let b: i32 = 20;
//     println!("{}",(a+b));
// }

// fn main() {
//     let length:i32 = 76;
//     let width:i32 = 45;
//     let area = length * width;
//     println!("The Area of the given Rectangle is {}",area);

// }

// fn main() {
//     let radius:f64 = 8.9;
//     let pi:f64 = 3.14;
//     let area:f64 = pi*(radius*radius);
//     println!("The Area of the given Circle is {:.3}",area);
// }   

// fn main() {
//     let a = "Code";
//     let b = "Chef";
//     println!("{}{}",a,b);
// }

// fn main() {
//     let x = true;
//     let y = false;
//     println!("{}",x);
//     print!("{}",y);
// }

// fn main() {
//     let side = 14;
//     let cost_per_cm = 7;
//     let area = side*side;
//     let total_cost = area * cost_per_cm;

//     println!("{}", area);
//     println!("{}$", total_cost);
// }

// fn main() {
//     let a: i32 = -50;
//     let b: i32 = 40;

//     println!("{}", a+b);
//     println!("{}",a*b);
//     println!("{}",a/b);
// }

// fn main() {
//     let name = "Chef";
//     // let name:String = String::from("Chef");
//     println!("{}", name);
// }

// fn main() {
//     let fruit:&str = "Apple";
//     println!("{}", fruit);
// }

// fn main() {
//     let mut fruit:&str = "Orange"; 
//     println!("{}",fruit);
//     fruit = "Banana";
//     print!("{}",fruit);
// }

// fn main() {
//     let x = "Hello";
//     let y = "World";
//     let word = format!("{} {}",x,y);
//     println!("{}", word);

// }



// fn main() {
//     let num1:&str = "25";
//     let num2:&str = "69";
//     let result = format!("{}{}",num1,num2);
//     println!("{}",result);
// }

// fn main() {
//     let txt = "NumeroTres";
//     println!("The length of the word is: {}", txt.len());
// }

// fn main() {
//     let word = "Programming";
//     println!("{}",word.chars().nth(1).unwrap());
//     println!("{}",word.chars().nth(3).unwrap());
// }


// fn main() { 
//     let mut word = String::from("Ocygen");
//     let mut bytes = word.into_bytes();
//     bytes[1] = b'x';
//     word = String::from_utf8(bytes).unwrap();
//     println!("{}",word);
// }

// fn main() {
//     let s  = String::from("Hello");
//     let part = &s[0..2];
//     println!("{}", part);
// }

// fn main() {

//     let var = String::from("String");
//     println!("{}", &var[0..3]);  // Incorrect syntax for slicing the string
// }

// fn main() {
//     let mut s = String::from("bcc");
//     let mut s1 = s.into_bytes();
//     s1[2] = b'd';
//     s = String::from_utf8(s1).unwrap();
//     println!("{}",s);
// }




// use std::io::{self,Write};

// fn main() {
//     let mut s = String::new();

//     print!("Please enter your name: ");
//     io::stdout().flush().unwrap(); // Flush stdout to display the print message immediately

//     io::stdin()
//         .read_line(&mut s)
//         .expect("Failed to read line"); // Read user input

//     println!("Your name is: {}", s.trim());
// }


use std::io::{self,write};

fn main() {
    let mut name = String::new();
    
    println!("PLease enter your name: ");
    io::stdout().flush().unwrap();

    io::stdin()
        .read_line(&mut name)
        .except("Unknown Error");

    println!("Your name is : {} ", name.trim());
    
}