//
//  ViewController.swift
//  concentration
//
//  Created by 葉 思卿 on 2019/1/25.
//  Copyright © 2019年 葉 思卿. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBAction func clickCard(_ sender: UIButton) {
        flipCard(emoji: "🎃", button: sender)
  
}
    func flipCard(emoji: String, button:  UIButton){
        if button.currentTitle == emoji{
            button.setTitle("", for: UIControlState.normal)
            button.backgroundColor = #colorLiteral(red: 0, green: 0.5690457821, blue: 0.5746168494, alpha: 1)
        }
        else{
            button.setTitle(emoji, for: UIControlState.normal)
            button.backgroundColor = #colorLiteral(red: 1, green: 1, blue: 1, alpha: 1)
        }
    }
}
