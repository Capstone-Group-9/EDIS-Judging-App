/**
 *
 * @export
 * @interface Team
 */
export interface Team {
  /**
   *
   * @type {number}
   * @memberof Team
   */
  id: number;
  /**
   *
   * @type {string}
   * @memberof Team
   */
  name: string;
  /**
   *
   * @type {number}
   * @memberof Team
   */
  totalscore: number;
  /**
   *
   * @type {string}
   * @memberof Team
   */
  teamcategory: string;
  /**
   *
   * @type {Array<number>}
   * @memberof Team
   */
  scores: Array<number>;
}
