import { Injectable } from '@angular/core';
// import { Http } from '@angular/http';
import { HttpClientModule } from '@angular/common/http';


import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { map, filter, scan, reduce } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class DataService {
  // ROOT_URL = 'https://jsonplaceholder.typicode.com/photos/?id=1&id=2&id=3&id=4&id=5&id=6&id=7&id=8&id=9&id=10';
  ROOT_URL2 = 'http://127.0.0.1:5000/regions/';
  ROOT_URL = 'http://127.0.0.1:5000/';

  currentCountry = 'US';
  isDefault = true;

  myData: Observable<Data>;

  constructor(public http: HttpClient) {
    console.log('Data service connected...');

  }

  getPosts() {
    // this.currentCountry = this.getCountryCode('create new method');
    console.log(this.ROOT_URL, this.currentCountry);
    this.ROOT_URL2 = this.getCountryCode(this.ROOT_URL);
    return this.http.get<Data>(this.ROOT_URL); // ;
    // .map(res => res.json());
    // .subscribe(data => data) ;
    //  .pipe(map((response: any) => response));

    // .pipe(map((response: any) => response.json()));
  }

  getCountryCode(url) {
    if (this.isDefault === true) {
      return url;
    } else { return url + 'region/' + this.currentCountry ;  } }


  setLocation(name: string) {
    this.currentCountry = name;
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
