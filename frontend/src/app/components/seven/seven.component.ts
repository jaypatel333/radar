import { Component, OnInit } from '@angular/core';
import { DataService } from '../../services/data.service';
import { toPublicName } from '@angular/compiler/src/i18n/serializers/xmb';

@Component({
  selector: 'app-seven',
  templateUrl: './seven.component.html',
  styleUrls: ['./seven.component.css']
})
export class SevenComponent implements OnInit {

  topics: Data;

  constructor(private dataService: DataService) {

  }

  ngOnInit() {

    this.dataService.getPosts().subscribe((topics) => {

      this.topics = topics; // .stringify(posts);
      this.topics = this.delData(this.topics);

      console.log(this.topics);
    });
  }

  delData(abc: Data) {
    abc.trends = abc.trends.slice(6, 7); // this.temp;

    return abc;
  }

}



interface Data {
  _id: string;
  date_added: string;
  location_tag: string;
  trends: Trend[];
}

interface Trend {
  trend_id: string;
  trend_name: string;
  articles: Article[];

}

interface Article {
  article_URL: string;
  article_id: string;
  article_post_date: string;
  article_thumbnail: string;
  atrticle_title: string;

}
