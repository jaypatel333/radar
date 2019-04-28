import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';

@Component({
  selector: 'app-five',
  templateUrl: './five.component.html',
  styleUrls: ['./five.component.css']
})
export class FiveComponent implements OnInit {

  topics: Topic[];

  constructor(private dataService: DataService) {

  }

  ngOnInit() {

    this.dataService.getPosts().subscribe((topics) => {

      this.topics = topics; // .stringify(posts);
      this.topics = this.delData(this.topics);

      console.log(this.topics);
    });
  }

  delData(abc: Topic[]) {
    return abc.slice(0, 10);
  }

}




interface Topic {
  id: number;
  title: string;
  body: string;
  userId: number;
}
