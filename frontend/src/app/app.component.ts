import { Component, OnInit } from '@angular/core';
import { DataService } from './services/data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'Topic Radar';
  topics: Topic[] = [];
  loadComponent1 = false;
  countryName = 'USA';

  constructor(private dataService: DataService) {
    console.log('constructor ran..');

  }

  ngOnInit() {

    this.dataService.getPosts().subscribe((topics) => {

      this.topics = topics; // .stringify(posts);

      console.log(this.topics);
    });


  }

  getArticles(arg) {

    console.log(arg);
  }

  setLocation(country: string) {
    this.countryName = country;
    this.dataService.setLocation(country);
    this.dataService.getPosts().subscribe((topics) => {

      this.topics = topics; // .stringify(posts);

      console.log(this.topics);
      this.ngOnInit() ;
    });
  }





  loadMyChildComponent1() {
    this.loadComponent1 = true;
  }
}


interface Topic {
  id: number;
  title: string;
  body: string;
  userId: number;
}

