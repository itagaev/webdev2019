import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';

@Component({
  selector: 'app-child',
  templateUrl: './child.component.html',
  styleUrls: ['./child.component.css']
})
export class ChildComponent implements OnInit {
  @Input() title = '';
  @Input() numberArray: number[] = [];

  @Output() output = new EventEmitter();
  @Output() stringArray = new EventEmitter<string[]>();
  constructor() { }

  ngOnInit() {
  }


  sendMessage(){
    this.output.emit('Message from child');
  }
  sendStringArray(){
    this.stringArray.emit(['a', 'b', 'c'])
  }
}
