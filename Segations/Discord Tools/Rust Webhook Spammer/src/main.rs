use std::io::stdin;
use serde_json::Value;

static banner: &str = r#"
███████╗██████╗ ███████╗███████╗███████╗██╗  ██╗██╗████████╗
██╔════╝██╔══██╗██╔════╝██╔════╝██╔════╝██║  ██║██║╚══██╔══╝  
█████╗  ██████╔╝█████╗  █████╗  ███████╗███████║██║   ██║      
██╔══╝  ██╔══██╗██╔══╝  ██╔══╝  ╚════██║██╔══██║██║   ██║    
██║     ██║  ██║███████╗███████╗███████║██║  ██║██║   ██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝   ╚═╝ 
Created By FreeShit ║ Dev: segations#2344 & 0David#0822 ║ getfreeshit.today
"#;


static json: &str = r#"{"username": "WebSpammer FreeShit / getfreeshit.today","content": "{CONTENT}"}"#;


#[derive(Clone)]
struct State {
    url: String,
    message: String,
    amount: u32,
    threads: u32,
}

fn main() {
    let state = init();
    unsafe {spam(state)};
} // You Need {} to print banner

fn init() -> State {
    println!("{}", banner);
    println!("Webhook url: ");
    let mut url = "".to_string();
    stdin().read_line(&mut url).unwrap();
    println!("Message: ");
    let mut message = "".to_string();
    stdin().read_line(&mut message).unwrap();
    println!("Amount: ");
    let mut amounts = "".to_string();
    stdin().read_line(&mut amounts).unwrap();
    let amount: u32 = amounts.replace("\r", "").replace("\n", "").parse().unwrap_or_else(|_| {
        println!("Expected a number of messages, couldnt convert message to a number, using default value");
        1000
    });
    let mut threadss = "".to_string();
    println!("Threads: ");
    stdin().read_line(&mut threadss).unwrap();
    let threads: u32 = threadss.replace("\r", "").replace("\n", "").parse().unwrap_or_else(|_| {
        println!("Expected a number of messages, couldnt convert message to a number, using default value");
        50
    });

    State {
        url,
        message,
        amount,
        threads,
    }
}

unsafe fn spam(states: State) {
    for i in 0..states.threads {
        let state = states.clone();
        let handle = std::thread::spawn(move || {
            let nm = &state.amount / &state.threads;
            let client = reqwest::blocking::Client::new();
            let jsonn: Value = serde_json::from_str(&json.replace("{CONTENT}", &state.message.replace("\r", "").replace("\n", "").as_ref())).unwrap();
            for i in 0..nm {
                let status_res = client.post(&state.url)
                .json(&jsonn)
                .send().unwrap();
                println!("Message sent, status code: {}", status_res.status());
            }
        });
        handle.join();
    }
}