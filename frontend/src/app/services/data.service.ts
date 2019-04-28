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
  ROOT_URL = 'https://jsonplaceholder.typicode.com/photos/?id=1&id=2&id=3&id=4&id=5&id=6&id=7&id=8&id=9&id=10';
  ROOT_URL2 = 'https://jsonplaceholder.typicode.com/photos/?albumId=';

  currentCountry = '1';

  topic: Observable<Topic[]>;
  constructor(public http: HttpClient) {
    console.log('Data service connected...');

  }

  getPosts() {
    // this.currentCountry = this.getCountryCode('create new method');
    console.log(this.ROOT_URL2, this.currentCountry) ;
    return this.http.get<Topic[]>(this.ROOT_URL2 + this.currentCountry); // ;
    // .map(res => res.json());
    // .subscribe(data => data) ;
    //  .pipe(map((response: any) => response));

    // .pipe(map((response: any) => response.json()));
  }

  getCountryCode(name) {

    return 'US';

  }

  setLocation(name: string) {
    this.currentCountry = name;
  }


}

interface Topic {
  id: number;
  title: string;
  body: string;
  userId: number;
}
